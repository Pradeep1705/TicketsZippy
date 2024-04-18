import Vue from 'vue'
import VueRouter from 'vue-router'
import LoginView from '../view/LoginView.vue'
import SignUpView from '../view/SignUpView.vue'
import homePageView from '../view/homePageView.vue'
import adminLogin from '../components/adminLogin.vue'
import userShow from '../components/userShow.vue'
import ticketBooking from '../components/ticketBooking.vue'
import userSearch from '../components/userSearch.vue'
import createVenue  from '../components/createVenue.vue'
import adminVenue from '../components/adminVenue.vue'
import editVenue from '../components/editVenue.vue'
import createShow from '../components/createShow.vue'
import adminShow from '../components/adminShow.vue'
import editShow from '../components/editShow.vue'
import userProfile from '../components/userProfile.vue'
import exportPage from '../components/exportPage.vue'
import jwt_decode from 'jwt-decode'

Vue.use(VueRouter)

const routes = [
    {
        path: '/register',
        name: 'SignUp',
        component: SignUpView,
    },
    {
        path: '/exportPage/:venueID',
        name: 'export',
        component: exportPage
    },
    {
        path: '/',
        name: 'Login',
        component: LoginView,
    },
    {
        path: '/home',
        name: 'home',
        component: homePageView,
        meta: { requiresAuth: true, requiresAdmin: false }
    },
    {
        path: '/adminLogin',
        name: 'adLogin',
        component: adminLogin,
    },
    {
        
        path: '/shows/:venueID',
        name: 'shows',
        component: userShow,
        meta: { requiresAuth: true, requiresAdmin: false }
    },
    {
        path: '/bookTicket/:showID/:venueID',
        name: 'booking',
        component: ticketBooking,
        meta: { requiresAuth: true, requiresAdmin: false }
    },
    {
        path: '/search/:keyword',
        name: 'search',
        component: userSearch,
        meta: { requiresAuth: true, requiresAdmin: false }
    },
    {
        path: '/createVenue',
        name: 'createVenue',
        component: createVenue,
        meta: { requiresAuth: true, requiresAdmin: true }
    },
    {
        path: '/adminVenue',
        name: 'adminVenue',
        component: adminVenue,
        meta: { requiresAuth: true, requiresAdmin: true },
    },
    {
        path: '/editVenue/:venueID',
        name: 'editVenue',
        component: editVenue,
        meta: { requiresAuth: true, requiresAdmin: true }
    },
    {
        path: '/createShow/:venueID',
        name: 'createShow',
        component: createShow,
        meta: { requiresAuth: true, requiresAdmin: true }
    }, 
    {
        path: '/adminShow/:venueID',
        name: 'adminShow',
        component: adminShow,
        meta: { requiresAuth: true, requiresAdmin: true }
    },
    {
        path: '/editShow/:showID/:venueID',
        name: 'editShow',
        component: editShow,
        meta: { requiresAuth: true, requiresAdmin: true }
    },
    {
        path: '/userProfile',
        name: 'userProfile',
        component: userProfile,
        meta: { requiresAuth: true, requiresAdmin: false }
    }
]

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
  })



function verifyToken(token){
    try{
        const decoded = jwt_decode(token)
        return decoded
    }catch(error){
        console.error(error)
        return null
    }
}

router.beforeEach((to, from, next)=> {
    const isAuthenticated = localStorage.getItem('token')
    const isAdmin = localStorage.getItem('user_type') === 'admin'

    if(to.matched.some(record => record.meta.requiresAuth)){
        if(isAuthenticated === 'null'){
            alert('Please Login to continue')
            next({path: '/'})
        }else{
            try{
                const decodedToken = verifyToken(isAuthenticated)
                if(decodedToken && decodedToken.exp * 1000 > Date.now()){
                    if(to.matched.some(record => record.meta.requiresAdmin)&& !isAdmin){
                        alert(' ACCESS DENIED!!')
                        next({path: '/home'})
                    }else{
                        next()
                    }
                }else{
                    alert('Session expired!!')
                    next({path: '/'})
                }
            }catch(error){
                console.error(error)
                next({path: '/'})
            }
        }
    }else{
        next()
    }
})

export default router;

