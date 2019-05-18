SOURCEDIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

USER_OTLS="${HOME}/"$(basename ${SOURCEDIR})"/otls"
PROD_HDAS="$( cd ${SOURCEDIR} >/dev/null 2>&1 && cd ../../ && cd hdas && pwd )"

before=`pwd`
cd $PROD_HDAS

for f in *.{hda,hdanc}
do
  if [ -f $f ]
  then
    echo "Copied" $f "to" "${USER_OTLS}/${f}"
    cp $f "${USER_OTLS}/${f}"
  fi
done

cd $before
