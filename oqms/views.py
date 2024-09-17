from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Quiz, Question, Answer, QuizAttempt, StudentAnswer
from .forms import QuizForm, QuestionForm, AnswerForm

# View for instructors to create a quiz
@login_required
def create_quiz(request):
    if request.user.groups.filter(name='Instructor').exists():
        if request.method == 'POST':
            form = QuizForm(request.POST)
            if form.is_valid():
                quiz = form.save(commit=False)
                quiz.instructor = request.user
                quiz.save()
                return redirect('quiz_list')
        else:
            form = QuizForm()
        return render(request, 'quiz/create_quiz.html', {'form': form})
    else:
        return redirect('instructor_quiz_list')

# View for students to take a quiz
@login_required
def take_quiz(request, quiz_id):
    if request.user.groups.filter(name='Student').exists():
        quiz = get_object_or_404(Quiz, pk=quiz_id)
        if request.method == 'POST':
            questions = quiz.questions.all()
            score = 0
            total_questions = questions.count()

            # Create the quiz attempt
            attempt = QuizAttempt.objects.create(student=request.user, quiz=quiz, score=0)

            for question in questions:
                selected_answer_id = request.POST.get(str(question.id))
                if selected_answer_id:
                    selected_answer = get_object_or_404(Answer, pk=selected_answer_id)

                    # Save student's answer
                    StudentAnswer.objects.create(attempt=attempt, question=question, selected_answer=selected_answer)

                    if selected_answer.is_correct:
                        score += 1

            # Calculate percentage score
            if total_questions > 0:
                score_percentage = (score / total_questions) * 100
            else:
                score_percentage = 0

            # Update the score in the QuizAttempt instance
            attempt.score = score_percentage
            attempt.save()

            return redirect('quiz_result', attempt_id=attempt.id)

        return render(request, 'quiz/take_quiz.html', {'quiz': quiz})
    else:
        return redirect('quiz_list')

# View for showing quiz results
@login_required
def quiz_result(request, attempt_id):
    attempt = get_object_or_404(QuizAttempt, pk=attempt_id, student=request.user)
    return render(request, 'quiz/quiz_result.html', {'attempt': attempt})

# View to list all available quizzes for students
@login_required
def quiz_list(request):
    if request.user.groups.filter(name='Student').exists():
        quizzes = Quiz.objects.all()
        return render(request, 'quiz/quiz_list.html', {'quizzes': quizzes})
    else:
        return redirect('instructor')

# View for instructors to list quizzes they have created
@login_required
def instructor_quiz_list(request):
    if request.user.groups.filter(name='Instructor').exists():
        quizzes = Quiz.objects.filter(instructor=request.user)
        return render(request, 'quiz/instructor_quiz_list.html', {'quizzes': quizzes})
    else:
        return redirect('home')

# View for instructors to add questions to quizzes
@login_required
def add_questions(request, quiz_id):
    if request.user.groups.filter(name='Instructor').exists():
        quiz = get_object_or_404(Quiz, pk=quiz_id)

        if request.method == 'POST':
            question_form = QuestionForm(request.POST)
            answer_forms = [AnswerForm(request.POST, prefix=str(i)) for i in range(4)]

            if question_form.is_valid() and all([form.is_valid() for form in answer_forms]):
                # Create and save the question
                question = question_form.save(commit=False)
                question.quiz = quiz
                question.save()

                # Create and save the answers
                for form in answer_forms:
                    answer = form.save(commit=False)
                    answer.question = question
                    answer.save()

                return redirect('add_questions', quiz_id=quiz.id)
        else:
            question_form = QuestionForm()
            answer_forms = [AnswerForm(prefix=str(i)) for i in range(4)]  # Four answers by default

        return render(request, 'quiz/add_questions.html', {
            'quiz': quiz,
            'question_form': question_form,
            'answer_forms': answer_forms,
        })
    else:
        return redirect('instructor')

@login_required
def quiz_questions(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id, instructor=request.user)
    questions = quiz.questions.all()

    return render(request, 'quiz/quiz_questions.html', {
        'quiz': quiz,
        'questions': questions,
    })

