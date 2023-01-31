import { createRouter, createWebHistory } from "vue-router";
import store from "@/api/store";

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: "/404",
      name: "NotFound",
      component: () => import("@/components/ETC/NotFound.vue")
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
      component: () => import("@/components/TheWelcome.vue")
    },
    {
      path: "/login",
      name: "LoginAddress",
      component: () => import("@/components/auth/LoginAddress.vue")
    },
    {
      path: "/signin",
      name: "SigninAddress",
      component: () => import("@/components/auth/SigninAddress.vue")
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
