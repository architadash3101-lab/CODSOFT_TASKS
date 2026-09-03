/**
 * script.js — UI controller. Reads all game logic from the global TTT (engine.js):
 * board state, minimax search, move selection. This file only renders and wires clicks.
 */
"use strict";
const T = TTT;

let board = Array(9).fill(T.EMPTY);
let humanSymbol = T.X, aiSymbol = T.O;
let humanTurn = true, over = false, lastAI = -1;
let totals = { you: 0, ai: 0, tie: 0 }, totalNodes = 0;

// ---------- AI move (engine call) ----------
function aiMove(){
  T.nodeCount = 0;
  const best = T.aiBestMoves(board, aiSymbol, humanSymbol);
  totalNodes += T.nodeCount;
  return best[Math.floor(Math.random() * best.length)]; // random among optimal moves
}

// ---------- rendering ----------
const $ = id => document.getElementById(id);
const svgFor = (s, c) =>
  s === T.X
    ? `<svg viewBox="0 0 100 100"><path d="M27 27 L73 73 M73 27 L27 73" stroke="${c}" stroke-width="11" stroke-linecap="round" fill="none"/></svg>`
    : `<svg viewBox="0 0 100 100"><circle cx="50" cy="50" r="26" stroke="${c}" stroke-width="11" fill="none"/></svg>`;

function render(){
  const bd = $('board'); bd.innerHTML = '';
  const w = T.winner(board);
  const winLine = w ? T.LINES.find(l => board[l[0]] === w && board[l[0]] === board[l[1]] && board[l[0]] === board[l[2]]) : null;
  board.forEach((v, i) => {
    const c = document.createElement('div');
    c.className = 'cell' + (v ? ' locked' : '') + (winLine && winLine.includes(i) ? ' win' : '') + (i === lastAI ? ' last' : '');
    c.innerHTML = v === T.X ? svgFor(T.X, '#38bdf8') : v === T.O ? svgFor(T.O, '#fb7185') : '';
    c.addEventListener('click', () => humanClick(i));
    bd.appendChild(c);
  });
  $('nodes').textContent = `Last search · ${T.nodeCount.toLocaleString()} nodes`;
  $('statsLine').textContent = `total ${totalNodes.toLocaleString()} nodes evaluated`;
  $('sYou').textContent = totals.you;
  $('sAI').textContent = totals.ai;
  $('sTie').textContent = totals.tie;
}

function setStatus(html, cls){
  const s = $('status');
  s.className = 'status' + (cls ? ' ' + cls : '');
  s.innerHTML = html;
}

// ---------- game flow ----------
function finish(w){
  over = true;
  if (w === humanSymbol){ totals.you++; setStatus('You won — but minimax should prevent this!', 'goal'); }
  else if (w === aiSymbol){ totals.ai++; setStatus('AI wins — it saw this several moves ahead.', 'lose'); }
  else { totals.tie++; setStatus('Draw — the best result humans can achieve vs minimax.', 'draw'); }
  render();
}

function checkEnd(){
  const w = T.winner(board);
  if (w){ finish(w); return true; }
  if (T.full(board)){ finish(0); return true; }
  return false;
}

function humanClick(i){
  if (over || !humanTurn || board[i] !== T.EMPTY) return;
  board[i] = humanSymbol; lastAI = -1; render();
  if (checkEnd()) return;
  humanTurn = false;
  setStatus('AI is thinking… <span class="pill">α-β</span>');
  setTimeout(aiTurn, 140);
}

function aiTurn(){
  if (over) return;
  const i = aiMove();
  board[i] = aiSymbol; lastAI = i; humanTurn = true; render();
  setStatus('Your turn — you play <b style="color:' + (humanSymbol === T.X ? '#38bdf8' : '#fb7185') + '">' + (humanSymbol === T.X ? 'X' : 'O') + '</b>');
  if (checkEnd()) return;
}

function reset(){
  board = Array(9).fill(T.EMPTY); over = false; lastAI = -1;
  render();
  if (humanSymbol === T.O){
    humanTurn = false;
    setStatus('AI moves first… <span class="pill">α-β</span>');
    setTimeout(aiTurn, 180);
  } else {
    humanTurn = true;
    setStatus('Your turn — you play <b style="color:#38bdf8">X</b>');
  }
}

function setSide(sym){
  humanSymbol = sym; aiSymbol = sym === T.X ? T.O : T.X;
  $('btnX').classList.toggle('active', sym === T.X);
  $('btnO').classList.toggle('active', sym === T.O);
  reset();
}

$('btnX').addEventListener('click', () => setSide(T.X));
$('btnO').addEventListener('click', () => setSide(T.O));
$('reset').addEventListener('click', reset);
reset();
