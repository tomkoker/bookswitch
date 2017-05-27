
import axios from 'axios'

export default {

  user: {
    authenticated: false
  },

  checkAuth: function(){
    var self = this;
    return new Promise((resolve, reject) => {
      axios.get('/api/me')
      .then((response) => {
        self.user.authenticated = response.data.data.authenticated;
        resolve(self.user);
      })
      .catch((error) => {
        console.log(error);
        reject(error);
      });
    });
  }
}

