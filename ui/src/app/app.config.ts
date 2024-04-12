import { ApplicationConfig } from '@angular/core';
import { provideRouter } from '@angular/router';

import { USER_ROUTES } from './app.routes';

export const appConfig: ApplicationConfig = {
  providers: [provideRouter(USER_ROUTES)]
};
