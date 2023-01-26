<template>
  <v-app :theme="theme">
    <v-app-bar app>
      <v-spacer></v-spacer>

      <v-btn
          :prepend-icon="theme === 'light' ? 'mdi-weather-sunny' : 'mdi-weather-night'"
          @click="onClick"
      >Toggle Theme</v-btn>
    </v-app-bar>
  </v-app>
</template>
<script setup>
import { ref } from "vue";

const theme = ref("light");

function onClick () {
  theme.value = theme.value === "light" ? "dark" : "light";
}
</script>