<template>
  <div>
    <h3>Our services:</h3>
    <div class="actions">
      <form ref="form" @submit="handleSubmit">
        <input type="search" name="query" v-model="query" placeholder="Search..."/>

        <select style="margin-left: 20px" name="sort_by" v-model="sort_by" @change="handleSubmit">
          <option selected value=""></option>
          <option value="name">Sort by name</option>
          <option value="price">Sort by price</option>
        </select>
        </form>
    </div>
    <ul>
      <li v-for="p in products" :key="p.id">
        <router-link :to="`/product/${p.slug}`">{{ p.name }} - ${{p.price}}</router-link>
      </li>
    </ul>
  </div>
</template>

<script>
import {useProductStore} from "@/stores/product";
import {mapState} from "pinia";

export default {
  name: "HomeView",
  setup() {
    let productStore = useProductStore()
    return {productStore}
  },
  data() {
    return {
      query: "",
      sort_by: ""
    }
  },
  beforeRouteUpdate(to, from) {
    this.get_products(to.query)
  },
  mounted() {
    this.get_products(this.$route.query)
  },
  computed: {
    ...mapState(useProductStore, ['products'])
  },
  methods: {
    get_products(params) {
      this.query = params.query;
      this.sort_by = params.sort_by;
      if (this.query || this.sort_by) {
        this.productStore.search_products(this.query, this.sort_by);
      } else {
        this.productStore.get_products();
      }
    },
    handleSubmit(e) {
      e.preventDefault();
      this.$router.push({ path: '/', query: { query: this.query, sort_by: this.sort_by }})
    }
  }
}
</script>

<style lang="css">
.actions {
  display: flex;
}
</style>
