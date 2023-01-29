import {createStore} from "vuex";

export default createStore({
  state: {
    userName: "",
    accessToken: "",
    refreshToken: "",
  },
  getters: {
    isLogin(state, userNaem) {
      return state.userName = userNaem;
    },
    clearUserName(state) {
      state.userName = "";
    },
    setToken(state, accessToken, refreshToken) {
      state.accessToken = accessToken;
      state.refreshToken = refreshToken;
    }
  },
});

