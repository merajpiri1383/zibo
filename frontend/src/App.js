import {BrowserRouter,Routes,Route} from "react-router-dom";
import "./static/form.css";
import "./static/App.css";
import Main from "./pages/main";
import Settings from "./pages/settings";
import AddProduct from "./components/settings/addProduct";
import Navbar from "./components/navbar";
const App = ()=> {
  return (
      <BrowserRouter>
          <Navbar />
          <Routes>
              <Route path="/" element={<Main />} />
              <Route path="/settings" element={<Settings />}>
                <Route path="add-product" element={<AddProduct />} />
              </Route>
          </Routes>
      </BrowserRouter>
  )
};export default App ;