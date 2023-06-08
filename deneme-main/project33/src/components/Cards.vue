<template>
  <v-card flat rounded="0">
    <v-window v-model="onboarding">
      <v-window-item :key="1" :value="1">
        <v-card
          :height="windowHeight - 130"
          class="d-flex justify-center align-center"
        >
          <div
            style="
              display: flex;
              flex-flow: column nowrap;
              align-items: center;
              flex-direction: row;
              flex-wrap: nowrap;
              margin: 50px;
            "
          >
            <v-img
              aspect-ratio="1/1"
              :width="windowWidth / 2"
              cover
              src="@/pictures/1.jpg"
            ></v-img>
            <p
              style="
                margin: 30px;
                color: black;
                font-family: 'tohoma', sans-serif;
              "
            >
              Tiroid kanserinin erken ve doğru tanısı, tedavi ve sağkalım
              oranını yükseltmektedir. Günümüzde Yapay Zekanın bir alt alanı
              olan Makine Öğrenmesi yöntemleri Bilgisayar Destekli Tanı
              sistemlerinde yaygın bir şekilde kullanılmaktadır.
              Gerçekleştirilecek bu proje çalışmasında, ülkemizde bulunan bir
              sağlık kuruluşundan alınan 500’den fazla örneklem veri üzerinde
              makine öğrenmesi teknikleri kullanılarak tiroid tanısı için bir
              Karar Destek Sistemi geliştirilecektir. Yapılan literatür
              taramasında birbirinden farklı 19 verinin kullanıldığı bir proje
              tespit edilememiştir. Bu projede 19 farklı nitelik incelenecektir.
              Bu 19 nitelik tek tek değerlendirildiğinde hastanın kanser tespiti
              zorlaşmaktadır. Bazı nitelikler hastanın yüksek oranda kanser
              olduğunu söylerken bazı nitelikler düşük oranda kanser olduğunu
              söylemektedir. Bu durum doktorların kararlarını etkilemektedir.
              Yapılacak bu proje ile bu tutarsızlığın ortadan kaldırılması
              hedeflenmektedir. Gerçekleştirilecek proje çalışması ile
              doktorlara ek görüş sunacak bir karar destek sisteminin
              sunulmasının yanı sıra hastalara hızlı teşhis konulması ve
              hastaların tedavi sürecinin hızlandırılması amaçlanmaktadır. Aynı
              zamanda gerçekleştirilecek projenin kullanımı için Web tabanlı ara
              yüz tasarımı yapılması da hedeflenmektedir.
            </p>
          </div>
        </v-card>
      </v-window-item>
      <v-window-item :key="2" :value="2">
        <v-card
          :height="windowHeight - 125"
          class="d-flex justify-center align-center"
        >
          <span class="text-h2"> Card 2 </span>
        </v-card>
      </v-window-item>
      <v-window-item :key="3" :value="3">
        <v-card
          :height="windowHeight - 125"
          class="d-flex justify-center align-center"
        >
          <span class="text-h2"> Card 3 </span>
        </v-card>
      </v-window-item>
    </v-window>

    <v-card-actions class="justify-space-between">
      <v-btn variant="plain" icon="mdi-chevron-left" @click="prev"></v-btn>
      <v-item-group v-model="onboarding" class="text-center" mandatory>
        <v-item
          v-for="n in length"
          :key="`btn-${n}`"
          v-slot="{ isSelected, toggle }"
          :value="n"
        >
          <v-btn
            :variant="isSelected ? 'outlined' : 'text'"
            icon="mdi-record"
            @click="toggle"
          ></v-btn>
        </v-item>
      </v-item-group>
      <v-btn variant="plain" icon="mdi-chevron-right" @click="next"></v-btn>
    </v-card-actions>
  </v-card>
</template>

<script>
export default {
  data: () => ({
    length: 3,
    onboarding: 0,
    windowHeight: window.innerHeight,
    windowWidth: window.innerWidth,
  }),

  methods: {
    next() {
      this.onboarding =
        this.onboarding + 1 > this.length ? 1 : this.onboarding + 1;
    },
    prev() {
      this.onboarding =
        this.onboarding - 1 <= 0 ? this.length : this.onboarding - 1;
    },
    onResize() {
      this.windowHeight = window.innerHeight;
      this.windowWidth = window.innerWidth;
    },
  },
  mounted() {
    this.$nextTick(() => {
      window.addEventListener("resize", this.onResize);
    });
  },

  beforeDestroy() {
    window.removeEventListener("resize", this.onResize);
  },
};
</script>
