import axios from 'axios';

const API_URL = 'http://127.0.0.1:5000';

export default {
  getBars() {
    return axios.get(`${API_URL}/quote/bars`);
  },
};
