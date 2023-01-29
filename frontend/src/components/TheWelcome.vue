<template>
    <v-row align="center" justify="center">
      <v-col cols="8">
        <v-banner elevation="5" outlined class="primary--text" align="center">Make your BLOG to NFT</v-banner>
        <br>
        <v-btn
            block
            depressed
            elevation="4"
            large
            text
            x-large
        ><router-link style="text-decoration: none; color: inherit;" to="/login">Login or Register</router-link></v-btn>
        <br>
        <v-carousel style="height: auto; width: auto;" hide-delimiters :show-arrows="false" cycle="true" interval=3000>
          <v-carousel-item
              v-for="(item,i) in items"
              :key="i"
              :src="item.src"
              reverse-transition="fade-transition"
              transition="fade-transition"
          ></v-carousel-item>
        </v-carousel>
      </v-col>
    </v-row>
</template>
<script>
export default {
  props: {
    theme: {
      type: String,
      default: "light",
    }
  },
  data() {
    return {
      items: [
        {
          src: "/nft.jpg"
        },
        {
          src: "/klaytn.jpg"
        },
        {
          src: "/ethereum.png"
        }
      ]
    };
  }
};
</script>