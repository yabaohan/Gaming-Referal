import React from 'react';
import {
  BrowserRouter as Router,
  Route,
  Link
} from 'react-router-dom';

//components
import Header from './component/headerComponent/header';
import Footer from './component/headerComponent/footerComponent/footer';
import HomePage from './component/headerComponent/pages/homePage';
import Products from './component/headerComponent/pages/products';

import './Assets/scss/default.scss';



function App() {
  return (
    <Router>
    <div className="App">
       
       <Header/>

       <Route exact path='/' component={HomePage} />
       <Route exact path='/Products' component={Products} />

       <Footer/>
    </div>
    </Router>
  );
}

export default App;
