import axios from 'axios';

const API_URL = 'http://localhost:5000';

export default {
  // Busca todos os usuários
  getUsers() {
    return axios.get(`${API_URL}/user`);
  },
  
  // Busca um usuário específico
  getUser(username) {
    return axios.get(`${API_URL}/user/${username}`);
  },
  
  // Adiciona um novo usuário
  addUser(user) {
    return axios.post(`${API_URL}/user`, user);
  },
  
  // Atualiza os dados de um usuário
  updateUser(username, user) {
    return axios.put(`${API_URL}/user/${username}`, user);
  },
  
  // Remove um usuário
  deleteUser(username) {
    return axios.delete(`${API_URL}/user/${username}`);
  },
};
