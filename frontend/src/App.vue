<template>
  <v-app :theme="this.theme">
    <NavBar v-model:theme="theme" @onclick="this.theme = $event"></NavBar>
    <TheWelcome></TheWelcome>
    <NavFooter></NavFooter>
  </v-app>
</template>
<script>
import NavBar from "@/components/layout/NavBar.vue";
import NavFooter from "@/components/layout/NavFooter.vue";
import TheWelcome from "@/components/TheWelcome.vue";

export default {
  data() {
    return {
      theme: "light",
    };
  },
  components: {
    TheWelcome,
    NavBar,
    NavFooter
  }
};

</script>