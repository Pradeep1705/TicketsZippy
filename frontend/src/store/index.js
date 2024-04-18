import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'
import router from '../routes'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    user_id: localStorage.getItem('user_id') || null,
    token: localStorage.getItem('token') || null,
    userType:  localStorage.getItem('user_type') || null,
  },
  getters: {
    USER_ID(state) {
      return state.user_id
    },
    TOKEN(state) {
      return state.token
    },
    USER_TYPE(state) {
      return state.userType
    }
  },
  mutations: {
    SIGNUP_MUTATION(state, payload) {
      state.token = payload.data.token
      state.user_id = payload.user_id
    },
    LOGIN_MUTATION(state, payload) {
      state.token = payload.data.token
      state.user_id = payload.user_id
      state.userType = payload.data?.userType
    },
    AdminLOGIN_MUTATION(state, payload){
        state.token = payload.data.token
        state.userType = payload.data?.userType
    },
    LOGOUT_MUTATION(state) {
      state.token = null
      state.userType = null
    },
  },
  actions: {
    async SIGNUP_ACTION({ commit }, payload) {
      try {
        const { data } = await axios.post('http://localhost:5000/register', payload)
        localStorage.setItem('token', data.token)
        localStorage.setItem('user_type', data.userType)
        const user_id = JSON.parse(atob(data.token.split('.')[1])).u_id
        localStorage.setItem('user_id', user_id)
        router.push('/')
        commit('SIGNUP_MUTATION', {data, user_id})
      } catch (error) {
        console.log(error)
      }
    },
    async LOGIN_ACTION({ commit }, payload) {
      try {
        const { data } = await axios.post('http://localhost:5000/login', payload)
        if (data.message === 'Invalid') {
          alert('Invalid Credentials')
          return
        }
        localStorage.setItem('token', data.token)
        localStorage.setItem('user_type', data.userType)

        console.log(data)
        const user_id = JSON.parse(atob(data.token.split('.')[1])).u_id
        localStorage.setItem('user_id', user_id)
        router.push('/home')
        commit('LOGIN_MUTATION', { data, user_id  })
      } catch (error) {
        console.log(error)
      }
    },

    async AdminLOGIN_ACTION({ commit }, payload) {
        try {
          const { data } = await axios.post('http://localhost:5000/adminLogin', payload)
          if (data.message === 'Invalid') {
            alert('Invalid Credentials')
            return
          }
          localStorage.setItem('token', data.token)
          localStorage.setItem('user_type', data.userType)
          console.log(data)
          router.push('/adminVenue')
          commit('AdminLOGIN_MUTATION', { data })
        } catch (error) {
          console.log(error)
        }
      },

    LOGOUT_ACTION({ commit }) {
      commit('LOGOUT_MUTATION')
      localStorage.setItem('token','null')
      localStorage.setItem('user_type','null')
      router.push('/')
    },
  },
  modules: {
  }
})
