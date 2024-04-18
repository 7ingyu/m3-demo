import express from 'express';
const router = express.Router();
import artworkRouter from './artwork';
import authRouter from './auth';

router.use('/artwork', artworkRouter);
router.use('/auth', authRouter);

export default router;