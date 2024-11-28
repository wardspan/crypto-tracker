import React from 'react';
import { AppBar, Toolbar, Typography, Button, Box } from '@mui/material';
import { Link as RouterLink } from 'react-router-dom';

const Navbar = () => {
  return (
    <AppBar position="static">
      <Toolbar>
        <Typography variant="h6" component="div" sx={{ flexGrow: 1 }}>
          Crypto Tracker
        </Typography>
        <Box>
          <Button color="inherit" component={RouterLink} to="/">
            Dashboard
          </Button>
          <Button color="inherit" component={RouterLink} to="/portfolio">
            Portfolio
          </Button>
          <Button color="inherit" component={RouterLink} to="/alerts">
            Alerts
          </Button>
          <Button color="inherit" component={RouterLink} to="/news">
            News
          </Button>
        </Box>
      </Toolbar>
    </AppBar>
  );
};

export default Navbar; 