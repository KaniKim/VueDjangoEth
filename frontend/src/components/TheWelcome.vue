<template>
    <v-row align="center" justify="center">
      <v-col cols="8">
        <h1 align="center" style="color:black;">Make your BLOG to NFT</h1>
        <v-carousel style="width:70%;height:40%" hide-delimiters :show-arrows="false" cycle="true" interval=3000>
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