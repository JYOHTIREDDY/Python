import React, { useState } from 'react';
import './App.css'; // Import CSS file for styling

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [otp, setOtp] = useState('');
  const [action, setAction] = useState('');

  const handleActionSelect = (selectedAction) => {
    setAction(selectedAction);
  };

  const handleLoginOrSignup = () => {
    if (action === 'login') {
      // Handle login
    } else if (action === 'signup') {
      // Handle signup
      if (otp) {
        // If OTP is provided, proceed with signup verification
        fetch("/signup", {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ username, email, password, otp })
        })
        .then(response => {
          if (response.ok) {
            setIsLoggedIn(true);
          } else {
            alert('Invalid OTP');
          }
        })
        .catch(error => {
          console.error('Error:', error);
        });
      } else {
        // If OTP is not provided, request OTP verification
        fetch("/signup/request-otp", {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ email })
        })
        .then(response => {
          if (response.ok) {
            alert('OTP sent to your email. Please check your inbox.');
          } else {
            alert('Failed to send OTP');
          }
        })
        .catch(error => {
          console.error('Error:', error);
        });
      }
    }
  };

  const handleLogout = () => {
    setIsLoggedIn(false);
    setUsername('');
    setEmail('');
    setPassword('');
    setOtp('');
    setAction('');
  };

  return (
    <div className="container">
      <div className="login-box">
        {isLoggedIn ? (
          <div>
            <h2 className="welcome-text">Welcome, {username}!</h2>
            <button className="logout-btn" onClick={handleLogout}>Logout</button>
          </div>
        ) : (
          <div>
            {!action && (
              <div>
                <button className="action-btn" onClick={() => handleActionSelect('login')}>Login</button>
                <button className="action-btn" onClick={() => handleActionSelect('signup')}>Signup</button>
              </div>
            )}
            {action === 'login' && (
              <div>
                {/* Login form */}
              </div>
            )}
            {action === 'signup' && (
              <div>
                {/* Signup form */}
                <div>
                  <label className="input-label" htmlFor="username">Username:</label>
                  <input
                    type="text"
                    id="username"
                    value={username}
                    onChange={(e) => setUsername(e.target.value)}
                    className="input-field"
                  />
                </div>
                <div>
                  <label className="input-label" htmlFor="email">Email:</label>
                  <input
                    type="email"
                    id="email"
                    value={email}
                    onChange={(e) => setEmail(e.target.value)}
                    className="input-field"
                  />
                </div>
                <div>
                  <label className="input-label" htmlFor="password">Password:</label>
                  <input
                    type="password"
                    id="password"
                    value={password}
                    onChange={(e) => setPassword(e.target.value)}
                    className="input-field"
                  />
                </div>
                {otp ? (
                  <div>
                    <label className="input-label" htmlFor="otp">Enter OTP:</label>
                    <input
                      type="text"
                      id="otp"
                      value={otp}
                      onChange={(e) => setOtp(e.target.value)}
                      className="input-field"
                    />
                  </div>
                ) : null}
                <button className="login-btn" onClick={handleLoginOrSignup}>
                  {otp ? 'Verify OTP' : 'Request OTP'}
                </button>
              </div>
            )}
          </div>
        )}
      </div>
    </div>
  );
}

export default App;




// import React, { useState } from 'react';
// import './App.css'; // Import CSS file for styling

// function App() {
//   const [isLoggedIn, setIsLoggedIn] = useState(false);
//   const [username, setUsername] = useState('');
//   const [email, setEmail] = useState('');
//   const [password, setPassword] = useState('');
//   const [action, setAction] = useState('');

//   const handleActionSelect = (selectedAction) => {
//     setAction(selectedAction);
//   };

//   const handleLoginOrSignup = () => {
//     fetch("/login", {
//       method: 'POST',
//       headers: {
//         'Content-Type': 'application/json'
//       },
//       body: JSON.stringify({ username, email, password, action })
//     })
//     .then(response => {
//       if (response.ok) {
//         setIsLoggedIn(true);
//       } else {
//         alert('Invalid username, email, or password');
//       }
//     })
//     .catch(error => {
//       console.error('Error:', error);
//     });
//   };

//   const handleLogout = () => {
//     setIsLoggedIn(false);
//     setUsername('');
//     setEmail('');
//     setPassword('');
//     setAction('');
//   };

//   return (
//     <div className="container">
//       <div className="login-box">
//         {isLoggedIn ? (
//           <div>
//             <h2 className="welcome-text">Welcome, {username}!</h2>
//             <button className="logout-btn" onClick={handleLogout}>Logout</button>
//           </div>
//         ) : (
//           <div>
//             {!action && (
//               <div>
//                 <button className="action-btn" onClick={() => handleActionSelect('login')}>Login</button>
//                 <button className="action-btn" onClick={() => handleActionSelect('signup')}>Signup</button>
//               </div>
//             )}
//             {action === 'login' && (
//               <div>
//                 <h2 className="login-text">Login</h2>
//                 <div>
//                   <label className="input-label" htmlFor="email">Email:</label>
//                   <input
//                     type="email"
//                     id="email"
//                     value={email}
//                     onChange={(e) => setEmail(e.target.value)}
//                     className="input-field"
//                   />
//                 </div>
//                 <div>
//                   <label className="input-label" htmlFor="password">Password:</label>
//                   <input
//                     type="password"
//                     id="password"
//                     value={password}
//                     onChange={(e) => setPassword(e.target.value)}
//                     className="input-field"
//                   />
//                 </div>
//                 <button className="login-btn" onClick={handleLoginOrSignup}>Login</button>
//               </div>
//             )}
//             {action === 'signup' && (
//               <div>
//                 <h2 className="login-text">Signup</h2>
//                 <div>
//                   <label className="input-label" htmlFor="username">Username:</label>
//                   <input
//                     type="text"
//                     id="username"
//                     value={username}
//                     onChange={(e) => setUsername(e.target.value)}
//                     className="input-field"
//                   />
//                 </div>
//                 <div>
//                   <label className="input-label" htmlFor="email">Email:</label>
//                   <input
//                     type="email"
//                     id="email"
//                     value={email}
//                     onChange={(e) => setEmail(e.target.value)}
//                     className="input-field"
//                   />
//                 </div>
//                 <div>
//                   <label className="input-label" htmlFor="password">Password:</label>
//                   <input
//                     type="password"
//                     id="password"
//                     value={password}
//                     onChange={(e) => setPassword(e.target.value)}
//                     className="input-field"
//                   />
//                 </div>
//                 <button className="login-btn" onClick={handleLoginOrSignup}>Signup</button>
//               </div>
//             )}
//           </div>
//         )}
//       </div>
//     </div>
//   );
// }

// export default App;

