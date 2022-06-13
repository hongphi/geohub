import { defineStore } from 'pinia'
import api from "@/api";

export const useProductStore = defineStore({
  id: 'services',
  state: () => ({
    products: [],
    product: null
  }),
  getters: {

  },
  actions: {
    get_products() {
      api.get("/api/services/").then((res) => {
        this.products = res.data;
      })
    },
    get_product(slug: string) {
      this.product = null;
      api.get(`/api/services/${slug}/`).then((res) => {
        this.product = res.data;
      })
    },
    search_products(query: string, sort_by: string) {
      api.get(`/api/services/?query=${query}&sort_by=${sort_by}`).then((res) => {
        this.products = res.data;
      })
    }
  }
})
