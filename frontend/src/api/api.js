import Axios from "@/api/axios";

function registerUser(userData) {
  return Axios.post("api/user/", userData);
}

function loginUser(userData) {
  return Axios.post("api/user/login/", userData);
}

export {registerUser, loginUser};