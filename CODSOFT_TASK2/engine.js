/**
 * engine.js — pure Tic-Tac-Toe game engine: Minimax + Alpha-Beta Pruning.
 * NO DOM, NO UI. Works in the browser (global `TTT`) and in Node (module),
 * so the exact same code can be unit-tested exhaustively with:
 *     node test_unbeatable.js
 */
"use strict";

const EMPTY = 0, X = 1, O = 2;
const LINES = [[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]];
const PREF  = [4,0,2,6,8,1,3,5,7]; // center -> corners -> edges (pruning-friendly order)

let nodeCount = 0;

function winner(b){
  for (const l of LINES){
    const v = b[l[0]];
    if (v && v === b[l[1]] && v === b[l[2]]) return v; // X or O, else 0
  }
  return 0;
}

function full(b){
  return b.every(c => c !== EMPTY);
}

/**
 * Depth-adjusted minimax with alpha-beta pruning.
 *   AI win  : +10 - depth   (sooner wins score higher)
 *   AI loss : -10 + depth   (later losses score higher)
 *   draw    :  0
 */
function minimax(b, depth, alpha, beta, maximizing, ai, hu, prune){
  nodeCount++;
  const w = winner(b);
  if (w) return w === ai ? 10 - depth : -10 + depth;
  if (full(b)) return 0;
  if (maximizing){                                  // AI to move — maximize
    let best = -Infinity;
    for (const i of PREF){
      if (b[i]) continue;
      b[i] = ai;
      const v = minimax(b, depth + 1, alpha, beta, false, ai, hu, prune);
      b[i] = EMPTY;
      if (v > best) best = v;
      if (v > alpha) alpha = v;
      if (prune && beta <= alpha) break;            // α-β cutoff
    }
    return best;
  } else {                                          // opponent to move — minimize
    let best = Infinity;
    for (const i of PREF){
      if (b[i]) continue;
      b[i] = hu;
      const v = minimax(b, depth + 1, alpha, beta, true, ai, hu, prune);
      b[i] = EMPTY;
      if (v < best) best = v;
      if (v < beta) beta = v;
      if (prune && beta <= alpha) break;
    }
    return best;
  }
}

/** All equally-optimal moves for `ai` from position `b` (each guarantees the same score). */
function aiBestMoves(b, ai, hu){
  let bestVal = -Infinity, best = [];
  for (const i of PREF){
    if (b[i]) continue;
    b[i] = ai;
    const v = minimax(b, 1, -Infinity, Infinity, false, ai, hu, true);
    b[i] = EMPTY;
    if (v > bestVal){ bestVal = v; best = [i]; }
    else if (v === bestVal){ best.push(i); }
  }
  return best;
}

const TTT = { EMPTY, X, O, LINES, PREF, winner, full, minimax, aiBestMoves };
Object.defineProperty(TTT, 'nodeCount', { get(){ return nodeCount; }, set(v){ nodeCount = v; } });

if (typeof module !== 'undefined' && module.exports) module.exports = TTT;
