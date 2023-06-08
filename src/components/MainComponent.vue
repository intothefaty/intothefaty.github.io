<template>
  <div>
    <v-toolbar
      dark
      prominent
      image="https://cdn.vuetifyjs.com/images/backgrounds/vbanner.jpg"
    >
      <v-toolbar-title style="color: aliceblue"
        ><b
          >Makine Öğrenmesi Teknikleri ile Tiroid Kanseri Tanısı: Bir Karar
          Destek Sistemi</b
        ></v-toolbar-title
      >

      <v-spacer></v-spacer>

    </v-toolbar>
  </div>
  <div>
    <UseModel></UseModel>
  </div>
</template>

<script>
import Cards from "./Cards.vue";
import UseModel from "./UseModel.vue";

export default {
    components: {
        Cards,
        UseModel,
    },
    data: () => ({
  }),
};
</script>
