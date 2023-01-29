import { createRouter, createWebHistory } from "vue-router";
import TheWelcome from "@/components/TheWelcome.vue";
import LoginAddress from "@/components/auth/LoginAddress.vue";
import SigninAddress from "@/components/auth/SigninAddress.vue";
import NotFound from "@/components/ETC/NotFound.vue";
import store from "@/api/store";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/404",
      name: "NotFound",
      component: NotFound
    },
    {
      path: "/:pathMatch(.*)*",
      redirect: "/404",
    },
    {
      path: "/",
      redirect: "/welcome"
    },
    {
      path: "/welcome",
      name: "TheWelcome",
      component: TheWelcome
    },
    {
      path: "/login",
      name: "LoginAddress",
      component: LoginAddress,
    },
    {
      path: "/signin",
      name: "SigninAddress",
      component: SigninAddress
    }
  ],
});

router.beforeEach(async(to, from, next) => {
  if (store.state.accessToken === null && store.state.refreshToken !== null) {
    await store.dispatch("refreshToken");
  }
  
  if (store.state.accessToken !== null) {
    return next();
  }
  
  if (store.state.accessToken === null && store.state.refreshToken === null) {
    return next({name: "LoginAddress"});
  }
  return next("/");
});

export default router;
