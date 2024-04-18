<template>

    <b-navbar toggleable="lg" type="danger" variant="info">
    <b-navbar-brand href="#">NavBar</b-navbar-brand>

    <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

    <b-collapse id="nav-collapse" is-nav>
      <b-navbar-nav>
        <b-nav-item href="#">Link</b-nav-item>
        
      </b-navbar-nav>

      <!-- Right aligned nav items -->
      <b-navbar-nav class="ml-auto">
        <b-nav-form @submit="onSubmit">
          <b-form-input v-model="form.searchQuery" size="sm" class="mr-sm-2" placeholder="Search"></b-form-input>
          <b-button  size="sm" class="my-2 my-sm-2" type="submit">Search</b-button>


          <br><br>
          <b-button  variant="secondary" class="my-2 my-sm-2" size="sm" ><router-link to="/login">Logout</router-link></b-button>

        </b-nav-form>

        

        
      </b-navbar-nav>
    </b-collapse>
  </b-navbar>

</template>

<script>


export default {
    
    data() {
      return {
        form: {
          searchQuery: '',
        },
      }
    },
    
    methods: {
      onSubmit(event) {
        event.preventDefault()
        let url = `/search/${this.form.searchQuery}`;
        console.log(url)
        console.log(this.form.searchQuery)
        // console.log(payload)
        this.$router.push(url);
       
      },
    }
}
</script>  