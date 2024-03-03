import {BrowserRouter,Routes,Route} from "react-router-dom";
import "./static/App.css";
import Main from "./pages/main";
import Settings from "./pages/settings";
import Navbar from "./components/navbar";
const App = ()=> {
  return (
      <BrowserRouter>
          <Navbar />
          <Routes>
              <Route path="/" element={<Main />} />
              <Route path="settings/" element={<Settings />} />
          </Routes>
      </BrowserRouter>
  )
};export default App ;