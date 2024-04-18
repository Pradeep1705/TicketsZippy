<template>
  <div>
    <userLogin />
    
  </div>
</template>






<script>

// import axios from 'axios'
import userLogin from '../components/userLogin.vue'

export default {
    name: 'logIn',
    components: {userLogin},
    data() {
      return {
        form: {
          username: '',
          password:'',
          
        },
        show: true
      }
    },
    methods: {
      onSubmit(event) {
        event.preventDefault()
        let payload = {"username":this.form.username,"password":this.form.password}
        console.log(payload)
        // axios.post('http://127.0.0.1:5000/login', payload)
        this.$router.push('/home')
      },
      onReset(event) {
        event.preventDefault()
        // Reset our form values
        this.form.email = ''
        this.form.username = ''
        this.form.password=''
        // Trick to reset/clear native browser form validation state
        this.show = false
        this.$nextTick(() => {
          this.show = true
        })
      }
    }
  }



</script>

