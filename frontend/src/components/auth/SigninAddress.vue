<template>
  <br>
  <br>
  <br>
    <v-container fluid style="max-width: 60%;">
      <v-flex md8 sm8>
        <v-card class="elevation-6">
          <v-toolbar color="gray" dark fluid>
            <v-toolbar-title>Sign In form</v-toolbar-title>
          </v-toolbar>
          <v-form id="check-login-form">
            <v-card-text>
              <v-col align="center">
                <v-text-field
                    v-model="email"
                    label="Login"
                    name="login"
                    style="max-width: 80%;"
                    type="text"
                ></v-text-field>
                <v-text-field
                    v-model="address"
                    label="Ethereum Address"
                    name="address"
                    style="max-width: 80%;"
                    type="text"
                ></v-text-field>
                <v-text-field
                    v-model="password"
                    label="Password"
                    name="password"
                    style="max-width: 80%;"
                    type="password"
                ></v-text-field>
              </v-col>
            </v-card-text>
          </v-form>
          <v-card-actions>
            <v-btn
                block
                color="gray"
                form="check-login-form"
                size="large"
                type="submit"
                variant="elevated"
            >
              Sign In
            </v-btn>
          </v-card-actions>
          <br>
        </v-card>
      </v-flex>
    </v-container>
</template>
<script>

export default {
  props: {
    theme: {
      type: String,
      default: "light",
    }
  },
  name: "SigninAddress",
  data: () => ({
    email: null,
    password: null,
    address: null,
    isError: false,
    errMsg: "",
  }),
  methods: {
  }
};
</script>
