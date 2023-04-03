const auth_srv_ip = 'http://rats.works:2069';

window.onload = () => {
  axios.defaults.baseURL = auth_srv_ip;
  if (document.getElementById('login-button')) {
    let login_button = document.getElementById('login-button');
    login_button.addEventListener('click', login);
  }
  if (document.getElementById('register-button')) {
    let register_button = document.getElementById('register-button');
    register_button.addEventListener('click', register);
  }
}

function login(event) {
  let ref_box = document.getElementById('ref-box');
  let password_box = document.getElementById('password-box');

  let ref = ref_box.value;
  let password = password_box.value;
  
  let config = {
    headers: {
      Ref: ref,
      Password: password
    }
  }
  axios.head('/login', config)
    .then(function(response) {
      switch (response.status) {
        case 200:
          // login success
          let bearer = refresh_bearer();
          document.cookie = "name=Bearer; value="+bearer+"; Secure";
          document.href = "/account";
        case 404:
          // bad username/email
        case 400:
          //bad password
      }
    });
}

function register(event) {
  alert(event);
}

function refresh_bearer() {
  axios.head('/refresh') {
    switch (response.status) {
      case 200:
        // refresh success
      case 401:
        // bad refresh JWT
  }
}
