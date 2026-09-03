#!/usr/bin/env node
/**
 * EXHAUSTIVE UNBEATABILITY TEST — runs against the REAL engine.js the browser uses.
 *
 * For the AI as FIRST and as SECOND player, enumerate EVERY legal game line:
 * the AI always plays its minimax-best move, while the opponent tries EVERY
 * legal reply at every turn. If no line ends in an AI loss, the AI provably
 * cannot lose against any strategy.
 *
 * Also measures how many nodes alpha-beta pruning saves vs plain minimax,
 * and verifies the game-theoretic result (empty board value = 0 = draw).
 *
 * Run with:  node test_unbeatable.js    (from this project folder)
 */
"use strict";
const TTT = require('./engine.js');
const { EMPTY, X, O, winner, full, minimax, aiBestMoves } = TTT;

function enumerateAll(b, turn, ai, hu, st){
  const w = winner(b);
  if (w || full(b)){
    if (w === ai) st.ai_win += 1;
    else if (w === hu) st.ai_loss += 1;
    else st.draw += 1;
    return;
  }
  if (turn === ai){                                 // AI plays its minimax-best move
    const i = aiBestMoves(b, ai, hu)[0];
    b[i] = ai;
    enumerateAll(b, hu, ai, hu, st);
    b[i] = EMPTY;
  } else {                                          // opponent branches over EVERY reply
    for (let i = 0; i < 9; i++){
      if (b[i] === EMPTY){
        b[i] = hu;
        enumerateAll(b, ai, ai, hu, st);
        b[i] = EMPTY;
      }
    }
  }
}

function prove(ai, hu, label){
  const st = { ai_win: 0, draw: 0, ai_loss: 0 };
  const t0 = Date.now();
  enumerateAll(Array(9).fill(EMPTY), X, ai, hu, st); // X always opens
  const dt = ((Date.now() - t0) / 1000).toFixed(2);
  const total = st.ai_win + st.draw + st.ai_loss;
  const ok = st.ai_loss === 0;
  console.log(
    `  AI as ${label.padEnd(15)} games=${String(total).padStart(5)}` +
    `   ai_win=${String(st.ai_win).padStart(5)}   draw=${String(st.draw).padStart(5)}` +
    `   ai_loss=${String(st.ai_loss).padStart(5)}   ->  ${ok ? 'PASS (unbeatable)' : 'FAIL <-- LOSING LINE FOUND'}   (${dt}s)`
  );
  return ok;
}

const line = '='.repeat(74);
console.log(line);
console.log(' EXHAUSTIVE UNBEATABILITY TEST — minimax + alpha-beta pruning (engine.js)');
console.log(line);
const ok1 = prove(X, O, 'X (first player)');
const ok2 = prove(O, X, 'O (second player)');

console.log('-'.repeat(74));
console.log(' Alpha-beta pruning measurement (from the empty board):');
const b = Array(9).fill(EMPTY);
TTT.nodeCount = 0;
const vAb = minimax(b, 0, -Infinity, Infinity, true, X, O, true);
const nAb = TTT.nodeCount;
TTT.nodeCount = 0;
const vNaive = minimax(b, 0, -Infinity, Infinity, true, X, O, false);
const nNaive = TTT.nodeCount;
const saved = nNaive - nAb;
console.log(`  empty board value = ${vAb}  (0 means draw under perfect play)`);
console.log(`  nodes explored with alpha-beta : ${String(nAb).padStart(8)}`);
console.log(`  nodes explored without pruning : ${String(nNaive).padStart(8)}`);
console.log(`  savings: ${String(saved).padStart(8)} nodes skipped (${(100 * (1 - nAb / nNaive)).toFixed(1)}% fewer)`);

const ggX = minimax(b, 0, -Infinity, Infinity, true, X, O, true);
const ggO = minimax(b, 0, -Infinity, Infinity, true, O, X, true);
const ok3 = ggX === 0 && ggO === 0 && vAb === vNaive;
console.log('-'.repeat(74));
console.log(` Game theory: value of empty board with X to maximize = ${ggX}, with O to maximize = ${ggO}`);
console.log(` Perfect play from the empty board is a ${ok3 ? 'DRAW' : 'non-draw'}.`);
console.log(line);
const passed = ok1 && ok2 && ok3;
console.log(passed ? ' ALL CHECKS PASSED — the AI never loses on any legal game line.'
                   : ' FAILURE — inspect the LOSING LINE and fix the engine.');
console.log(line);
process.exit(passed ? 0 : 1);
