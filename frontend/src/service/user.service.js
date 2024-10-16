import axios from "axios";

export default class UserService {
    static async getAll() {
        return axios.get("http://localhost:5000/users");
    }
    
    static async addUser(params) {
        return axios.post("http://localhost:5000/users", params);
    }

    static async editUser(id, params) {
        return axios.put(`http://localhost:5000/users/${id}`, params);
    }

    static async getUser(id) {
        return axios.get(`http://localhost:5000/users/${id}`);
    }

    static async deleteUser(id) {
        return axios.delete(`http://localhost:5000/users/${id}`);
    }
}