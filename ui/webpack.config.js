const { shareAll, withModuleFederationPlugin } = require('@angular-architects/module-federation/webpack');

module.exports = withModuleFederationPlugin({

  name: 'user-app',

  exposes: {
    // './Component': './projects/user/ui/src/app/app.component.ts',

    // Expose all the routes defined in user app to shell app
    './User-Routes': './projects/user/ui/src/app/app.routes.ts',
  },

  shared: {
    ...shareAll({ singleton: true, strictVersion: true, requiredVersion: 'auto' }),
  },

});
