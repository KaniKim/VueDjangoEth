import { createApp } from "vue";
import App from "./App.vue";
import "@mdi/font/css/materialdesignicons.css";

import "vuetify/styles";
import {createVuetify} from "vuetify";
import * as components from "vuetify/components";
import * as directives from "vuetify/directives";
import router from "./router";

const app = createApp(App);

const vuetify = createVuetify({
  icons: {
    iconfont: "mdi",
  },
  theme: {
    themes: {
    
    }
  },
  components,
  directives,
});

app.use(router);
app.use(vuetify);
app.mount("#app");

