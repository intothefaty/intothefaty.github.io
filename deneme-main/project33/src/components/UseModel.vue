<template>
  <div>
    <div
      style="
        background-color: #FFF2FE;
        width: 90%;
        margin-left: 5%;
        margin-right: 5%;
        margin-top: 2%;
        padding: 6%;
        padding-top: 3.5% !important;
        padding-bottom: 2% !important;
        border-style: solid;
        border-radius: 25px;
      "
    >
      <v-text-field
        v-model="age"
        label="Yaş"
        type="number"
        density="compact"
        variant="underlined"
      ></v-text-field>
      <v-row>
        <v-col>
          <v-select
            v-model="sex"
            item-title="text"
            item-value="val"
            label="Cinsiyet"
            :items="sex_list"
            density="compact"
            variant="underlined"
            return-object="true"
          ></v-select>
          <v-select
            v-model="story"
            item-title="text"
            item-value="val"
            label="Aile Öyküsü"
            :items="var_yok"
            density="compact"
            variant="underlined"
            return-object="true"
          ></v-select>
          <v-select
            v-model="r_story"
            item-title="text"
            item-value="val"
            label="Boyuna Radyasyon Öyküsü"
            :items="var_yok"
            density="compact"
            variant="underlined"
            return-object="true"
          ></v-select>
          <v-select
            v-model="pks"
            item-title="text"
            item-value="val"
            label="Prekanseröz Sendromlar"
            :items="var_yok"
            density="compact"
            variant="underlined"
            return-object="true"
          ></v-select>
          <v-select
            v-model="disfaji"
            item-title="text"
            item-value="val"
            label="Disfaji"
            :items="var_yok"
            density="compact"
            variant="underlined"
            return-object="true"
          ></v-select>
          <v-select
            v-model="dispne"
            item-title="text"
            item-value="val"
            label="Dispne"
            :items="var_yok"
            density="compact"
            variant="underlined"
            return-object="true"
          ></v-select>
          <v-select
            v-model="fast_growth_nodul"
            item-title="text"
            item-value="val"
            label="Hızlı Büyümüş Kitle"
            :items="var_yok"
            density="compact"
            variant="underlined"
            return-object="true"
          ></v-select>
          <v-select
            v-model="vkp"
            item-title="text"
            item-value="val"
            label="Vokal Kord Paralizisi"
            :items="var_yok"
            density="compact"
            variant="underlined"
            return-object="true"
          ></v-select>
          <v-select
            v-model="tsh"
            item-title="text"
            item-value="val"
            label="TSH Düzeyi"
            :items="d_n_y"
            density="compact"
            variant="underlined"
            return-object="true"
          ></v-select>
        </v-col>
        <v-col>
          <v-text-field
            v-model="usg_nodul"
            label="USG Nodül Çapı (enbüyük/mm)"
            type="number"
            density="compact"
            variant="underlined"
          ></v-text-field>
          <v-select
            v-model="ekojonite"
            item-title="text"
            item-value="val"
            label="Ekojonite"
            :items="hih"
            density="compact"
            variant="underlined"
            return-object="true"
          ></v-select>
          <v-select
            v-model="irregular_border"
            item-title="text"
            item-value="val"
            label="Düzensiz Sınır"
            :items="var_yok"
            density="compact"
            variant="underlined"
            return-object="true"
          ></v-select>
          <v-select
            v-model="microcalsification"
            item-title="text"
            item-value="val"
            label="Mikrokalsifikasyon"
            :items="var_yok"
            density="compact"
            variant="underlined"
            return-object="true"
          ></v-select>
          <v-select
            v-model="mth_width"
            item-title="text"
            item-value="val"
            label="Yüksek Genişlikten Fazla"
            :items="var_yok"
            density="compact"
            variant="underlined"
            return-object="true"
          ></v-select>
          <v-select
            v-model="extratiroial_sep"
            item-title="text"
            item-value="val"
            label="Ekstratiroial Yayılım"
            :items="var_yok"
            density="compact"
            variant="underlined"
            return-object="true"
          ></v-select>

          <!-- EU-TIRADS-->
          <v-select
            v-model="eu_tirads"
            item-title="text"
            item-value="val"
            label="EU-TIRADS"
            :items="eu_tirads_list"
            density="compact"
            variant="underlined"
            return-object="true"
          ></v-select>
          <v-select
            v-model="usg_patological_lap"
            item-title="text"
            item-value="val"
            label="USG'de Patolojik Lap"
            :items="var_yok"
            density="compact"
            variant="underlined"
            return-object="true"
          ></v-select>
          <v-select
            v-model="bethesta"
            label="İİAB: BETHESTA"
            :items="['1', '2', '3', '4', '5']"
            density="compact"
            variant="underlined"
          ></v-select>
        </v-col>
      </v-row>
      <div
        style="
          display: flex;
          justify-content: space-around;
        "
      >
        <v-btn
          @click="getResult()"
          elevation="7"
          color="#acebfc"
          rounded="xl"
          size="x-large"
        >
          SONUÇLANDIR
        </v-btn>
      </div>
    </div>
    <v-row
      style="
        width: 90%;
        margin-left: 5%;
        margin-right: 5%;
        margin-top: 1%;
        margin-bottom: 10%;
        padding: 1% !important;
        border-style: solid;
        border-radius: 25px;
        display: flex;
        justify-content: space-around;
        background-color: #FFF2FE;
      "
    >
      <h1>
        SONUÇ:
        {{
          this.result == 1
            ? "KANSER"
            : this.result == 0
            ? "KANSER DEĞİL"
            : "----"
        }}
      </h1>
    </v-row>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      result: null,
      // VALUE LISTS
      eu_tirads_list: [
        {
          text: "0",
          val: "0",
        },
        {
          text: "1",
          val: "1",
        },
        {
          text: "2",
          val: "2",
        },
        {
          text: "3",
          val: "3",
        },
        {
          text: "4",
          val: "4",
        },
        {
          text: "5",
          val: "5",
        },
      ],
      d_n_y: [
        {
          text: "Düşük",
          val: "0",
        },
        {
          text: "Normal",
          val: "1",
        },
        {
          text: "Yüksek",
          val: "2",
        },
      ],
      hih: [
        {
          text: "Hipoekoik",
          val: "0",
        },
        {
          text: "İzoekoik",
          val: "1",
        },
        {
          text: "Hiperekoik",
          val: "2",
        },
      ],
      var_yok: [
        {
          text: "Yok",
          val: "0",
        },
        {
          text: "Var",
          val: "1",
        },
      ],
      sex_list: [
        {
          text: "Kadın",
          val: "1",
        },
        {
          text: "Erkek",
          val: "2",
        },
      ],
      //DEFAULT VALUES
      age: 25,
      sex: {
        text: "Kadın",
        val: "1",
      },
      story: {
        text: "Yok",
        val: "0",
      },
      r_story: {
        text: "Yok",
        val: "0",
      },
      pks: {
        text: "Yok",
        val: "0",
      },
      disfaji: {
        text: "Yok",
        val: "0",
      },
      dispne: {
        text: "Yok",
        val: "0",
      },
      fast_growth_nodul: {
        text: "Yok",
        val: "0",
      },
      vkp: {
        text: "Yok",
        val: "0",
      },
      tsh: {
        text: "Normal",
        val: "1",
      },
      usg_nodul: 0,
      ekojonite: {
        text: "İzoekoik",
        val: "1",
      },
      irregular_border: {
        text: "Yok",
        val: "0",
      },
      microcalsification: {
        text: "Yok",
        val: "0",
      },
      mth_width: {
        text: "Yok",
        val: "0",
      },
      extratiroial_sep: {
        text: "Yok",
        val: "0",
      },
      eu_tirads: {
        text: "3",
        val: "3",
      },
      usg_patological_lap: {
        text: "Yok",
        val: "0",
      },
      bethesta: "1",
    };
  },
  methods: {
    getResult() {
      let tempStr =
        this.age.toString() +
        "," +
        this.sex.val +
        "," +
        this.story.val +
        "," +
        this.r_story.val +
        "," +
        this.pks.val +
        "," +
        this.disfaji.val +
        "," +
        this.dispne.val +
        "," +
        this.fast_growth_nodul.val +
        "," +
        this.vkp.val +
        "," +
        this.tsh.val +
        "," +
        this.usg_nodul +
        "," +
        this.ekojonite.val +
        "," +
        this.irregular_border.val +
        "," +
        this.microcalsification.val +
        "," +
        this.mth_width.val +
        "," +
        this.extratiroial_sep.val +
        "," +
        this.eu_tirads.val +
        "," +
        this.usg_patological_lap.val +
        "," +
        this.bethesta;
      console.log(tempStr);
      axios.get("http://localhost:8000/predict/" + tempStr).then((response) => {
        this.result = response.data;
        console.log(this.result);
      });
    },
  },
};
</script>
