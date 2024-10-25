import axios from 'axios';

const API_URL = 'http://127.0.0.1:5000';

export default {
  // Search all users
  getUsers() {
    return axios.get(`${API_URL}/user`);
  },
  
  // Search for a specific user
  getUser(user) {
    return axios.get(`${API_URL}/user/${user}`);
  },
  
  // Add a new user
  addUser(user) {
    return axios.post(`${API_URL}/user`, user);
  },
  
  // Update a user's data
  updateUser(user, username) {
    return axios.put(`${API_URL}/user/${username}`, user);
  },
  
  // Remove a user
  deleteUser(user) {
    return axios.delete(`${API_URL}/user/${user}`);
  },
};
