import signUpUser from './4-user-promise';
import uploadPhoto from './5-photo-reject';

export default function handleProfileSignup(firstName, lastName, fileName) {
  console.log('Starting handleProfileSignup');

  const user = signUpUser(firstName, lastName);
  const photo = uploadPhoto(fileName);
  const promises = [user, photo];

  console.log('Promises created:', promises);

  return Promise.allSettled(promises).then((results) => {
    console.log('All promises settled:', results);

    const finalResults = results.map((result) => ({
      status: result.status,
      value: result.status === 'fulfilled' ? result.value : result.reason,
    }));

    console.log('Final results:', finalResults);
    return finalResults;
  }).catch((error) => {
    console.error('Error in handleProfileSignup:', error);
  });
}
