<template>
    <v-app-bar app>
      <v-spacer></v-spacer>
      <v-btn
          :prepend-icon="theme === 'light' ? 'mdi-weather-sunny' : 'mdi-weather-night'"
          @click="onClick()"
          :value="theme"
      >Toggle Theme</v-btn>
    </v-app-bar>
</template>
<script>

export default {
  props: {
    theme: {
      type: String,
      default: "light",
    }
  },
  methods: {
    onClick() {
      if(this.theme == "light") {
        this.$emit("onclick", "dark");
      } else {
        this.$emit("onclick", "light");
      }
    }
  }
};
</script>