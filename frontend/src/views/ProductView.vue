<template>
  <div v-if="product">
    <h1>{{product.name}}</h1>
    <p>${{product.price}}</p>
    <button type="button">Buy</button>
  </div>
</template>

<script>
import {useProductStore} from "@/stores/product";
import {mapState} from "pinia";

export default {
  name: "ProductView",
  setup() {
    let productStore = useProductStore()
    return {productStore}
  },
  computed: {
    ...mapState(useProductStore, ['product'])
  },
  created() {
    this.productStore.get_product(this.$route.params.slug)
  },
  beforeRouteUpdate(to, from) {
    this.productStore.get_produtct(to.params.slug)
  }
}
</script>

<style scoped>

</style>
