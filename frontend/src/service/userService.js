import axios from 'axios';

const API_URL = 'http://127.0.0.1:5000';

export default {
  // Busca todos os usuários
  getUsers() {
    return axios.get(`${API_URL}/user`);
  },
  
  // Busca um usuário específico
  getUser(user) {
    return axios.get(`${API_URL}/user/${user}`);
  },
  
  // Adiciona um novo usuário
  addUser(user) {
    return axios.post(`${API_URL}/user`, user);
  },
  
  // Atualiza os dados de um usuário
  updateUser(user, username) {
    return axios.put(`${API_URL}/user/${username}`, user);
  },
  
  // Remove um usuário
  deleteUser(user) {
    return axios.delete(`${API_URL}/user/${user}`);
  },
};
