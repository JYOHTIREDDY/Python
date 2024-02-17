import React, { useState, useEffect } from 'react';

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = () => {
    fetch("/login", {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({ username, password })
    })
    .then(response => {
      if (response.ok) {
        setIsLoggedIn(true);
      } else {
        alert('Invalid username or password');
      }
    })
    .catch(error => {
      console.error('Error:', error);
    });
  };

  return (
    <div>
      {isLoggedIn ? (
        <div>
          <h2>Welcome, {username}!</h2>
          <button onClick={() => setIsLoggedIn(false)}>Logout</button>
        </div>
      ) : (
        <div>
          <h2>Login</h2>
          <div>
            <label htmlFor="username">Username:</label>
            <input type="text" id="username" value={username} onChange={(e) => setUsername(e.target.value)} />
          </div>
          <div>
            <label htmlFor="password">Password:</label>
            <input type="password" id="password" value={password} onChange={(e) => setPassword(e.target.value)} />
          </div>
          <button onClick={handleLogin}>Login</button>
        </div>
      )}
    </div>
  );
}

export default App;





// import React, { useState, useEffect } from 'react';

// function App() {
//   const [data, setData] = useState([]);

//   useEffect(() => {
//     fetch("/members")
//       .then(res => res.json())
//       .then(data => {
//         setData(data);
//         console.log(data);
//       })
//       .catch(error => {
//         console.error('Error fetching data:', error);
//       });
//   }, []);

//   return (
//     <div>
//       {(typeof data.members === 'undefined') ? (
//         <p>Loading  ....</p>
//       ) : (
//         data.members.map((member, i ) => (
//           <p key = {i}>{member}</p>
//         ))
//       )
//       }
//     </div>
//   );
// }

// export default App;
