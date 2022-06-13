import axios from "axios";

const api = axios.create({
  baseURL: 'http://localhost:8000',
  headers: {'Access-Control-Allow-Headers': '*'}
});

api.defaults.xsrfCookieName = 'csrftoken';
api.defaults.xsrfHeaderName = "HTTP_X_CSRFTOKEN";

export default api;
