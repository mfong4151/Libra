import React, {FC} from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import ImportCards from './components/ImportCards'
import OrganizeCards from './components/OrganizeCards'
import SelectDeck from './components/SelectDeck'
import NavBar from './components/NavBar';
import MainPage from './components/MainPage'
import ReviewDeck from './components/ReviewDeck';

const App:FC = () => {
  return (
      <main>
        <Router>
          <NavBar/>
          <div className='padding-default'>
            <Routes>
              <Route path='/' element={<MainPage/>} /> 
              <Route path='/import' element={<ImportCards/>}/>
              <Route path='/select' element={<SelectDeck/>}/>
              <Route path='/organize' element={<OrganizeCards/>}/>      
              <Route path='/review/:id' element={<ReviewDeck/>}/>      
            </Routes>
          </div>
        </Router>
      </main>
    
  );
};

export default App;