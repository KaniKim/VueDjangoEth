<template>
  <v-app :theme="this.theme">
    <NavBar v-model:theme="theme" @onclick="this.theme = $event"></NavBar>
    <RouterView v-model:theme="theme" @onclick="this.theme = $event"></RouterView>
    <NavFooter></NavFooter>
  </v-app>
</template>
<script>
import NavBar from "@/components/layout/NavBar.vue";
import NavFooter from "@/components/layout/NavFooter.vue";

export default {
  data() {
    return {
      theme: "light",
    };
  },
  components: {
    NavBar,
    NavFooter
  }
};

</script>