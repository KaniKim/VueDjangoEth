import axios from "axios";
import store from "@/api/store";

const Axios = axios.create({
  baseURL: import.meta.env.VITE_BASE_URL,
  headers: {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + store.state.accessToken
  },
});

Axios.interceptors.request.use((config) => {
  config.headers.Authorization = store.state.accessToken;
  return config;
}, (error) => {
  return Promise.reject(error);
});

Axios.interceptors.response.use((res) => {
  return res;
}, (err) => {
  return Promise.reject(err);
});

export default Axios;