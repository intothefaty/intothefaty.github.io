<template>
  <div
    style="width: 300px; display: flex; flex-wrap: nowrap; align-items: center"
  >
    <!-- Kayıt -->
    <v-row justify="center">
      <v-dialog v-model="dialog1" persistent width="30%">
        <template v-slot:activator="{ props }">
          <v-btn color="#E3F2FD" v-bind="props"> Üye Ol </v-btn>
        </template>
        <v-card>
          <v-card-title>
            <span class="text-h5">Üye Ol</span>
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-text-field
                label="Username"
                variant="underlined"
                dense
              ></v-text-field>
              <v-text-field
                label="E-Mail"
                variant="underlined"
                dense
              ></v-text-field>
              <v-text-field
                label="Phone Number"
                variant="underlined"
                dense
              ></v-text-field>
              <v-text-field
                :append-icon="show1 ? 'mdi-eye' : 'mdi-eye-off'"
                :type="show1 ? 'text' : 'password'"
                name="input-10-1"
                label="Password"
                variant="underlined"
                dense
                @click:append="this.show1 = !this.show1"
              ></v-text-field>
            </v-container>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              color="blue-darken-1"
              variant="text"
              @click="dialog1 = false"
            >
              Close
            </v-btn>
            <v-btn
              color="blue-darken-1"
              variant="text"
              @click="dialog1 = false"
            >
              Save
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>

    <!-- Üye Girişi -->
    <v-row justify="center" style="margin-top: -12px">
      <v-dialog v-model="dialog2" persistent width="30%">
        <template v-slot:activator="{ props }">
          <v-btn color="#E3F2FD" v-bind="props"> Üye Girişi </v-btn>
        </template>
        <v-card>
          <v-card-title>
            <span class="text-h5">Üye Girişi</span>
          </v-card-title>
          <v-card-text>
            <v-container>
              <v-text-field
                v-model="username"
                label="Username"
                variant="underlined"
                dense
              ></v-text-field>
              <v-text-field
                v-modeel="password"
                :append-icon="show2 ? 'mdi-eye' : 'mdi-eye-off'"
                :type="show2 ? 'text' : 'password'"
                name="input-10-1"
                label="Password"
                variant="underlined"
                dense
                @click:append="this.show2 = !this.show2"
              ></v-text-field>
            </v-container>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              color="blue-darken-1"
              variant="text"
              @click="dialog2 = false"
            >
              Close
            </v-btn>
            <v-btn
              color="blue-darken-1"
              variant="text"
              @click="memberValidation()"
            >
              Giriş
            </v-btn>
          </v-card-actions>
        </v-card>
      </v-dialog>
    </v-row>
  </div>
</template>

<script>
export default {
  components: {},
  data() {
    return {
      show1: false,
      show2: false,
      dialog1: false,
      dialog2: false,
      username: "",
      password: "",
      isMember: false,
    };
  },
  methods: {
    memberValidation() {
      // SQL username ve password kontrolü
      let memberControl = true;
      if (memberControl) {
        this.dialog2 = false;
        this.isMember = true;
        this.$emit('isMember',this.isMember)
      }
    },
  },
};
</script>
