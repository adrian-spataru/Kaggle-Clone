/* ============
 * Actions for the account module
 * ============
 *
 * The actions that are available on the
 * account module.
 */

import * as types from './mutation-types';

export const store = ({ commit }, payload) => {
  commit(types.STORE, payload);
};

export const clear = ({ commit }) => {
  commit(types.CLEAR);
};

export default {
  store,
  clear,
};
