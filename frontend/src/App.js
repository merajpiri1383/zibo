import {BrowserRouter,Routes,Route} from "react-router-dom";
import "./static/form.css";
import "./static/App.css";
import Main from "./pages/main";
import Settings from "./pages/settings";
import CreateProduct from "./components/settings/CreateProduct";
import CreateCategory from "./components/settings/CreateCategory";
import Navbar from "./components/navbar";
const App = ()=> {
  return (
      <BrowserRouter>
          <Navbar />
          <Routes>
              <Route path="/" element={<Main />} />
              <Route path="/settings" element={<Settings />}>
                <Route path="create-product" element={<CreateProduct />} />
                <Route path="create-category" element={<CreateCategory />} />
              </Route>
          </Routes>
      </BrowserRouter>
  )
};export default App ;