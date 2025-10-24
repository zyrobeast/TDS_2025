const quizEl = document.getElementById('quiz');
const questionEl = document.getElementById('question');
const choicesEl = document.getElementById('choices');
const prevBtn = document.getElementById('prev');
const nextBtn = document.getElementById('next');
const submitBtn = document.getElementById('submit');
const resultEl = document.getElementById('result');

const questions = [
  {
    id: 'q1',
    text: 'Which festival is called the festival of lights?',
    choices: ['Diwali','Holi','Eid','Baisakhi','Onam'],
    answerIndex: 0,
    explanation: 'Diwali is widely referred to as the Festival of Lights.'
  },
  {
    id: 'q2',
    text: 'Which festival is famous for throwing colors?',
    choices: ['Onam','Baisakhi','Holi','Eid','Diwali'],
    answerIndex: 2,
    explanation: 'Holi is the festival of colors.'
  },
  {
    id: 'q3',
    text: 'Which festival marks the Sikh New Year and is celebrated with harvest fairs?',
    choices: ['Eid','Baisakhi','Diwali','Holi','Onam'],
    answerIndex: 1,
    explanation: 'Baisakhi is a harvest festival celebrated especially in Punjab.'
  },
  {
    id: 'q4',
    text: 'Which festival is associated with the end of Ramadan?',
    choices: ['Diwali','Holi','Baisakhi','Eid','Onam'],
    answerIndex: 3,
    explanation: 'Eid al-Fitr marks the end of Ramadan.'
  },
  {
    id: 'q5',
    text: 'Which festival is a major harvest festival celebrated in Kerala?',
    choices: ['Onam','Diwali','Holi','Eid','Baisakhi'],
    answerIndex: 0,
    explanation: 'Onam is a harvest festival celebrated in Kerala.'
  }
];

let current = 0;
const answers = new Array(questions.length).fill(null);

function renderQuestion(i){
  const q = questions[i];
  questionEl.textContent = `${i+1}. ${q.text}`;
  choicesEl.innerHTML = '';
  q.choices.forEach((c, idx)=>{
    const li = document.createElement('li');
    li.className = 'choice';
    li.tabIndex = 0;
    li.textContent = c;
    if(answers[i] === idx) li.classList.add('selected');
    li.addEventListener('click', ()=> select(i, idx));
    li.addEventListener('keydown', (e)=>{ if(e.key === 'Enter') select(i, idx); });
    choicesEl.appendChild(li);
  });
  updateControls();
}

function select(qIndex, choiceIndex){
  answers[qIndex] = choiceIndex;
  renderQuestion(qIndex);
}

function updateControls(){
  prevBtn.disabled = current === 0;
  nextBtn.disabled = current === questions.length-1;
}

prevBtn.addEventListener('click', ()=>{
  if(current>0) current--;
  renderQuestion(current);
});
nextBtn.addEventListener('click', ()=>{
  if(current<questions.length-1) current++;
  renderQuestion(current);
});

submitBtn.addEventListener('click', ()=>{
  const unanswered = answers.reduce((acc,a,i)=> a===null ? acc.concat(i+1) : acc, []);
  if(unanswered.length){
    if(!confirm(`You have not answered questions: ${unanswered.join(', ')}. Submit anyway?`)) return;
  }
  grade();
});

function grade(){
  let score = 0;
  const lines = [];
  questions.forEach((q, i)=>{
    const chosen = answers[i];
    const correct = q.answerIndex;
    const ok = chosen === correct;
    if(ok) score++;
    lines.push(`${i+1}. ${q.text}\nYour answer: ${chosen==null? '—': q.choices[chosen]}\nCorrect: ${q.choices[correct]}${ok? ' ✅' : ' ❌'}\n${q.explanation}\n`);
  });
  resultEl.classList.remove('hidden');
  resultEl.innerHTML = `<strong>Score: ${score}/${questions.length}</strong><pre>${lines.join('\n')}</pre>`;
  resultEl.scrollIntoView({behavior:'smooth'});
}

// initial render
renderQuestion(current);

// keyboard shortcuts
document.addEventListener('keydown', (e)=>{
  if(e.key === 'ArrowRight') nextBtn.click();
  if(e.key === 'ArrowLeft') prevBtn.click();
});
