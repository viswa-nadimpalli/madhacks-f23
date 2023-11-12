import React, { useEffect, useState } from 'react';
import './quiz.css'
import './fonts/Ubuntu/Ubuntu-Bold.ttf';

interface QuizQuestion {
  id: number;
  type: string;
  question: string;
  options?: string[];
}

const QuizGenerator: React.FC = () => {
  const [numTrueFalse, setNumTrueFalse] = useState<number>(0);
  const [numMultipleChoice, setNumMultipleChoice] = useState<number>(0);
  const [numShortAnswer, setNumShortAnswer] = useState<number>(0);
  const [quizQuestions, setQuizQuestions] = useState<QuizQuestion[]>([]);





  const generateQuiz = () => {
    const questions: QuizQuestion[] = [];

    for (let i = 1; i <= numTrueFalse; i++) {
      questions.push({
        id: i,
        type: 'TrueFalse',
        question: `True/False Question ${i}`,
      });
    }

    for (let i = 1; i <= numMultipleChoice; i++) {
      questions.push({
        id: numTrueFalse + i,
        type: 'MultipleChoice',
        question: `Multiple Choice Question ${i}`,
        options: ['Option A', 'Option B', 'Option C', 'Option D'],
      });
    }

    for (let i = 1; i <= numShortAnswer; i++) {
      questions.push({
        id: numTrueFalse + numMultipleChoice + i,
        type: 'ShortAnswer',
        question: `Short Answer Question ${i}`,
      });
    }

    setQuizQuestions(questions);
  };

  const logoimg = document.querySelector('.quizStuff');
  logoimg && logoimg.classList.add('quizAni');

  return (
    <div className='top'>
        <div className='quizStuff'>
        <h1 id='startText'>Quiz Generator</h1>
        <div>
            <label>
            Number of True/False Questions:<br></br>
            <input
                type="number" 
                value={numTrueFalse}
                onChange={(e) => setNumTrueFalse(parseInt(e.target.value, 10))}
            />
            </label>
        </div>
        <div>
            <label>
            Number of Multiple Choice Questions:<br></br>
            <input
                type="number"
                value={numMultipleChoice}
                onChange={(e) => setNumMultipleChoice(parseInt(e.target.value, 10))}
            />
            </label>
        </div>
        <div>
            <label>
            Number of Short Answer Questions:<br></br>
            <input
                type="number"
                value={numShortAnswer}
                onChange={(e) => setNumShortAnswer(parseInt(e.target.value, 10))}
            />
            </label>
        </div>
        <button className='genButton' onClick={generateQuiz}>Generate Quiz</button>

        <div>
            <h2>Generated Quiz:</h2>
            <ul>
            {quizQuestions.map((question) => (
                <li key={question.id}>
                {`Q${question.id}: ${question.question} (${question.type})`}
                {question.options && (
                    <ul>
                    {question.options.map((option, index) => (
                        <li key={index}>{option}</li>
                    ))}
                    </ul>
                )}
                </li>
            ))}
            </ul>
        </div>
        </div>
    </div>
  );
};

export default QuizGenerator;