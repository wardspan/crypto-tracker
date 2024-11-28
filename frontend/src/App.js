import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { ThemeProvider, createTheme } from '@mui/material';
import CssBaseline from '@mui/material/CssBaseline';

import Layout from './components/layout/Layout';

// Lazy load pages
const Dashboard = React.lazy(() => import('./pages/Dashboard'));
const Portfolio = React.lazy(() => import('./pages/Portfolio'));
const Alerts = React.lazy(() => import('./pages/Alerts'));
const News = React.lazy(() => import('./pages/News'));

const theme = createTheme({
  palette: {
    mode: 'dark',
    primary: {
      main: '#90caf9',
    },
    secondary: {
      main: '#f48fb1',
    },
  },
});

function App() {
  return (
    <ThemeProvider theme={theme}>
      <CssBaseline />
      <Router>
        <Layout>
          <React.Suspense fallback={<div>Loading...</div>}>
            <Routes>
              <Route path="/" element={<Dashboard />} />
              <Route path="/portfolio" element={<Portfolio />} />
              <Route path="/alerts" element={<Alerts />} />
              <Route path="/news" element={<News />} />
            </Routes>
          </React.Suspense>
        </Layout>
      </Router>
    </ThemeProvider>
  );
}

export default App;
